// Datastructures.hh
//
// Student name:
// Student email:
// Student number:

#ifndef DATASTRUCTURES_HH
#define DATASTRUCTURES_HH

#include <string>
#include <vector>
#include <tuple>
#include <utility>
#include <limits>
#include <functional>
#include <exception>
#include <unordered_set>

// Types for IDs
using AffiliationID = std::string;
using PublicationID = unsigned long long int;
using Name = std::string;
using Year = unsigned short int;
using Weight = int;
struct Connection;
// Type for a distance (in arbitrary units)
using Distance = int;

using Path = std::vector<Connection>;
using PathWithDist = std::vector<std::pair<Connection,Distance>>;

// Return values for cases where required thing was not found
AffiliationID const NO_AFFILIATION = "---";
PublicationID const NO_PUBLICATION = -1;
Name const NO_NAME = "!NO_NAME!";
Year const NO_YEAR = -1;
Weight const NO_WEIGHT = -1;

// Return value for cases where integer values were not found
int const NO_VALUE = std::numeric_limits<int>::min();

// Type for a coordinate (x, y)
struct Coord
{
    int x = NO_VALUE;
    int y = NO_VALUE;
};

struct Affiliation {
    AffiliationID id; // Unique string ID
    Name name;  // Name of the affiliation
    Coord coord;

    Affiliation() : id(""), name(""), coord() {}

    Affiliation(AffiliationID id, const Name& name, Coord coord)
        : id(id), name(name), coord(coord) {}

    Coord getCoord() const{
        return coord;
    }
};

struct Publication {
    PublicationID id;
    Name name;
    Year year;
    std::vector<AffiliationID> affiliations;
    std::vector<PublicationID> references;

    Publication() : id(NO_PUBLICATION), name(NO_NAME), year(NO_YEAR) {}

    Publication(PublicationID id, const Name& name, Year year)
        : id(id), name(name), year(year) {}
};



// Example: Defining == and hash function for Coord so that it can be used
// as key for std::unordered_map/set, if needed
inline bool operator==(Coord c1, Coord c2) { return c1.x == c2.x && c1.y == c2.y; }
inline bool operator!=(Coord c1, Coord c2) { return !(c1==c2); } // Not strictly necessary

struct CoordHash
{
    std::size_t operator()(Coord xy) const
    {
        auto hasher = std::hash<int>();
        auto xhash = hasher(xy.x);
        auto yhash = hasher(xy.y);
        // Combine hash values (magic!)
        return xhash ^ (yhash + 0x9e3779b9 + (xhash << 6) + (xhash >> 2));
    }
};

// Example: Defining < for Coord so that it can be used
// as key for std::map/set
inline bool operator<(Coord c1, Coord c2)
{
    if (c1.y < c2.y) { return true; }
    else if (c2.y < c1.y) { return false; }
    else { return c1.x < c2.x; }
}

// Return value for cases where coordinates were not found
Coord const NO_COORD = {NO_VALUE, NO_VALUE};

struct Connection
{
    AffiliationID aff1 = NO_AFFILIATION;
    AffiliationID aff2 = NO_AFFILIATION;
    Weight weight = NO_WEIGHT;
    bool operator==(const Connection& c1) const{
        return (aff1==c1.aff1) && (aff2==c1.aff2) && (weight==c1.weight);
    }
};
const Connection NO_CONNECTION{NO_AFFILIATION,NO_AFFILIATION,NO_WEIGHT};


// Return value for cases where Distance is unknown
Distance const NO_DISTANCE = NO_VALUE;

// This exception class is there just so that the user interface can notify
// about operations which are not (yet) implemented
class NotImplemented : public std::exception
{
public:
    NotImplemented() : msg_{} {}
    explicit NotImplemented(std::string const& msg) : msg_{msg + " not implemented"} {}

    virtual const char* what() const noexcept override
    {
        return msg_.c_str();
    }
private:
    std::string msg_;
};

// This is the class you are supposed to implement

class Datastructures
{
public:
    Datastructures();
    ~Datastructures();

    // Estimate of performance: O(1)
    // Short rationale for estimate: The function simply returns the size of the affiliations unordered_map,
    // which should be constant time.
    unsigned int get_affiliation_count();

    // Estimate of performance: O(n)
    // Short rationale for estimate: Both affiliations and publications unordered_maps are cleared,
    // which should be linear time.
    void clear_all();

    // Estimate of performance: O(n)
    // Short rationale for estimate: The function needs to iterate over all affiliations to gather their IDs,
    // resulting in a linear time complexity.
    std::vector<AffiliationID> get_all_affiliations();

    // Estimate of performance: O(1)
    // Short rationale for estimate: Inserts a new affiliation into the affiliations unordered_map
    // using the unique ID as the key, which should be constant time.
    bool add_affiliation(AffiliationID id, Name const& name, Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    Name get_affiliation_name(AffiliationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    Coord get_affiliation_coord(AffiliationID id);


    // We recommend you implement the operations below only after implementing the ones above

    // Estimate of performance: O(n * log n)
    // Short rationale for estimate: The function sorts the affiliations based on names,
    // requiring a linear traversal of affiliations and a logarithmic sorting operation.
    std::vector<AffiliationID> get_affiliations_alphabetically();

    // Estimate of performance: O(n * log n)
    // Short rationale for estimate: The function calculates distances for each affiliation and then sorts them based
    // on these distances, resulting in a linear traversal and logarithmic sorting.
    std::vector<AffiliationID> get_affiliations_distance_increasing();

    // Estimate of performance: O(n)
    // Short rationale for estimate: The function iterates through affiliations to find the one with the specified coordinates,
    // resulting in a linear time complexity.
    AffiliationID find_affiliation_with_coord(Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    bool change_affiliation_coord(AffiliationID id, Coord newcoord);


    // We recommend you implement the operations below only after implementing the ones above

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    bool add_publication(PublicationID id, Name const& name, Year year, const std::vector<AffiliationID> & affiliations);

    // Estimate of performance: O(n)
    // Short rationale for estimate: The function needs to iterate over all publications to gather their IDs,
    // resulting in a linear time complexity.
    std::vector<PublicationID> all_publications();

    // Estimate of performance: O(1)
    // Short rationale for estimate: Is a direct lookup operation in the datastructure, which is constant time.
    Name get_publication_name(PublicationID id);

    // Estimate of performance: O(1)
    // Short rationale for estimate: Is a direct lookup operation in the datastructure, which is constant time.
    Year get_publication_year(PublicationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    std::vector<AffiliationID> get_affiliations(PublicationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    bool add_reference(PublicationID id, PublicationID parentid);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    std::vector<PublicationID> get_direct_references(PublicationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Uses find to go through the datastructure which is linear time.
    bool add_affiliation_to_publication(AffiliationID affiliationid, PublicationID publicationid);

    // Estimate of performance: O(n)
    // Short rationale for estimate: The function needs to iterate over all publications to find
    // those associated with a specific affiliation, resulting in a linear time complexity.
    std::vector<PublicationID> get_publications(AffiliationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: The function needs to iterate over all publications to find the parent
    // of a specific publication, resulting in a linear time complexity.
    PublicationID get_parent(PublicationID id);

    // Estimate of performance: O(n * log n)
    // Short rationale for estimate: The function filters and sorts publications based on affiliation and year,
    // resulting in a linear traversal and logarithmic sorting.
    std::vector<std::pair<Year, PublicationID>> get_publications_after(AffiliationID affiliationid, Year year);

    // Estimate of performance: O(n)
    // Short rationale for estimate: The function recursively traverses the referencing chain,
    // and the time complexity depends on the height of the tree (n).
    std::vector<PublicationID> get_referenced_by_chain(PublicationID id);


    // Non-compulsory operations

    // Estimate of performance:
    // Short rationale for estimate:
    std::vector<PublicationID> get_all_references(PublicationID id);

    // Estimate of performance:
    // Short rationale for estimate:
    std::vector<AffiliationID> get_affiliations_closest_to(Coord xy);

    // Estimate of performance:
    // Short rationale for estimate:
    bool remove_affiliation(AffiliationID id);

    // Estimate of performance:
    // Short rationale for estimate:
    PublicationID get_closest_common_parent(PublicationID id1, PublicationID id2);

    // Estimate of performance:
    // Short rationale for estimate:
    bool remove_publication(PublicationID publicationid);


    // PRG 2 functions:

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: the function has three nested loops so in the
    // worst case it will go through the whole n in every loop
    std::vector<Connection> get_connected_affiliations(AffiliationID id);

    // Estimate of performance: O(n^3)
    // Short rationale for estimate: the function has three nested loops so in the
    // worst case it will go through the whole n in every loop
    std::vector<Connection> get_all_connections();

    // Estimate of performance: O(n^3)
    // Short rationale for estimate: the function has three nested loops so in the
    // worst case it will go through the whole n in every loop
    Path get_any_path(AffiliationID source, AffiliationID target);

    // PRG2 optional functions

    // Estimate of performance:
    // Short rationale for estimate:
    Path get_path_with_least_affiliations(AffiliationID source, AffiliationID target);

    // Estimate of performance:
    // Short rationale for estimate:
    Path get_path_of_least_friction(AffiliationID source, AffiliationID target);

    // Estimate of performance:
    // Short rationale for estimate:
    PathWithDist get_shortest_path(AffiliationID source, AffiliationID target);


private:

    std::unordered_map<AffiliationID, Affiliation> affiliations;

    std::unordered_map<PublicationID, Publication> publications;

    std::unordered_set<AffiliationID> visited_ids;
};

#endif // DATASTRUCTURES_HH
