// Datastructures.cc
//
// Student name:
// Student email:
// Student number:

#include "datastructures.hh"

#include <random>

#include <cmath>

#include <unordered_set>

#include <iostream>

#include <queue>

std::minstd_rand rand_engine; // Reasonably quick pseudo-random generator

template <typename Type>
Type random_in_range(Type start, Type end)
{
    auto range = end-start;
    ++range;

    auto num = std::uniform_int_distribution<unsigned long int>(0, range-1)(rand_engine);

    return static_cast<Type>(start+num);
}

// Modify the code below to implement the functionality of the class.
// Also remove comments from the parameter names when you implement
// an operation (Commenting out parameter name prevents compiler from
// warning about unused parameters on operations you haven't yet implemented.)

Datastructures::Datastructures()
{
    std::unordered_map<AffiliationID, Affiliation> affiliations;

    std::unordered_map<PublicationID, Publication> publications;

    std::unordered_set<AffiliationID> visited_ids;
}

Datastructures::~Datastructures()
{
    // Write any cleanup you need here
}

unsigned int Datastructures::get_affiliation_count()
{
    // Replace the line below with your implementation
    return affiliations.size();
}

void Datastructures::clear_all()
{
    // Replace the line below with your implementation
    affiliations.clear();
    publications.clear();
}

std::vector<AffiliationID> Datastructures::get_all_affiliations()
{
    std::vector<AffiliationID> allAffiliations;
    std::transform(affiliations.begin(), affiliations.end(), std::back_inserter(allAffiliations),
                   [](const auto& pair) { return pair.first; });
    return allAffiliations;
}

bool Datastructures::add_affiliation(AffiliationID id, const Name& name, Coord xy)
{
    if (affiliations.find(id) != affiliations.end()) {
        return false; // Affiliation ID is not unique
    }
    affiliations[id] = Affiliation(id, name, xy);
    return true;
}

Name Datastructures::get_affiliation_name(AffiliationID id)
{
    auto it = affiliations.find(id);

    if (it != affiliations.end()) {
        return it->second.name;
    } else {
        return NO_NAME;
    }
}

Coord Datastructures::get_affiliation_coord(AffiliationID id)
{
    auto it = affiliations.find(id);

    if (it != affiliations.end()) {

        return it->second.coord;
    } else {
        return NO_COORD;
    }
}

std::vector<AffiliationID> Datastructures::get_affiliations_alphabetically()
{
    std::vector<Affiliation> sortedAffiliations;

    for (const auto& pair : affiliations) {
        sortedAffiliations.push_back(pair.second);
    }

    std::sort(sortedAffiliations.begin(), sortedAffiliations.end(),
              [](const Affiliation& a, const Affiliation& b) {
                  return a.name < b.name;
              });

    std::vector<AffiliationID> sortedAffiliationIDs;
    for (const auto& affiliation : sortedAffiliations) {
        sortedAffiliationIDs.push_back(affiliation.id);
    }

    return sortedAffiliationIDs;
}

std::vector<AffiliationID> Datastructures::get_affiliations_distance_increasing()
{
    // Create a vector of pairs from the map
    std::vector<std::pair<AffiliationID, double>> affiliationPairs;
    affiliationPairs.reserve(affiliations.size());

    // Populate the vector with AffiliationID and corresponding Coords
    for (const auto& [id, affiliation] : affiliations) {
        Coord xy = affiliation.coord;
        double distance = std::hypot(xy.x, xy.y); // Using hypot for better numerical stability
        affiliationPairs.emplace_back(id, distance);
    }

    // Sort the vector of pairs based on the distances
    std::sort(affiliationPairs.begin(), affiliationPairs.end(),
              [](const auto& a, const auto& b) {
                  return a.second < b.second;
              });

    // Create a vector of sorted AffiliationIDs
    std::vector<AffiliationID> DistanceSortedAffiliations;
    DistanceSortedAffiliations.reserve(affiliationPairs.size());

    // Extract the sorted AffiliationIDs
    std::transform(affiliationPairs.begin(), affiliationPairs.end(),
                   std::back_inserter(DistanceSortedAffiliations),
                   [](const auto& pair) {
                       return pair.first;
                   });

    return DistanceSortedAffiliations;
}

AffiliationID Datastructures::find_affiliation_with_coord(Coord xy)
{
    for (const auto& [id, affiliation] : affiliations) {
        if (affiliation.getCoord() == xy) {
            return id;
        }
    }

    return NO_AFFILIATION;
}

bool Datastructures::change_affiliation_coord(AffiliationID id, Coord newcoord)
{
    auto it = affiliations.find(id);
    if (it == affiliations.end()) {
        return false;
    }

    it->second.coord = newcoord;

    return true;
}

bool Datastructures::add_publication(PublicationID id, const Name &name, Year year, const std::vector<AffiliationID> &affiliations)
{
    if (publications.find(id) != publications.end()) {
        return false;
    }

    Publication publication(id, name, year);
    publication.affiliations = affiliations;
    publications[id] = publication;

    return true;
}

std::vector<PublicationID> Datastructures::all_publications()
{
    std::vector<PublicationID> allPublications;

    for (const auto& ID : publications) {
        allPublications.push_back(ID.first);
    }

    return allPublications;
}

Name Datastructures::get_publication_name(PublicationID id)
{
    auto it = publications.find(id);

    if (it != publications.end()) {
        return it->second.name;
    } else {
        return NO_NAME;
    }
}

Year Datastructures::get_publication_year(PublicationID id)
{
    auto it = publications.find(id);

    if (it != publications.end()) {

        return it->second.year;
    } else {
        return NO_YEAR;
    }
}

std::vector<AffiliationID> Datastructures::get_affiliations(PublicationID id)
{
    std::vector<AffiliationID> affiliationslist;
    auto it = publications.find(id);
    if (it != publications.end()) {
        affiliationslist = it->second.affiliations;
    }else {
        affiliationslist.push_back(NO_AFFILIATION);
    }

    return affiliationslist;
}

bool Datastructures::add_reference(PublicationID id, PublicationID parentid)
{
    auto it = publications.find(id);
    auto parent_it = publications.find(parentid);

    if (it == publications.end() && parent_it == publications.end()) {
        return false;
    }

    parent_it->second.references.push_back(id);
    return true;
}

std::vector<PublicationID> Datastructures::get_direct_references(PublicationID id)
{
    std::vector<PublicationID> publicationslist;
    auto it = publications.find(id);
    if (it != publications.end()) {
        publicationslist = it->second.references;
    }else {
        publicationslist.push_back(NO_PUBLICATION);
    }

    return publicationslist;
}

bool Datastructures::add_affiliation_to_publication(AffiliationID affiliationid, PublicationID publicationid)
{
    auto affiliation_it = affiliations.find(affiliationid);
    auto publication_it = publications.find(publicationid);

    if (affiliation_it == affiliations.end() || publication_it == publications.end()) {
        return false;
    }

    publication_it->second.affiliations.push_back(affiliationid);

    return true;
}

std::vector<PublicationID> Datastructures::get_publications(AffiliationID id)
{
    std::vector<PublicationID> publicationsList;


    if (affiliations.find(id) == affiliations.end()) {
        publicationsList.push_back(NO_PUBLICATION);
    }

    for (const auto& pub_pair : publications) {
        const Publication& publication = pub_pair.second;

        if (std::find(publication.affiliations.begin(), publication.affiliations.end(), id) != publication.affiliations.end()) {
            publicationsList.push_back(pub_pair.first);
        }
    }

    return publicationsList;
}
PublicationID Datastructures::get_parent(PublicationID id)
{
    for (const auto& pub_pair : publications) {
        const Publication& publication = pub_pair.second;
        if (std::find(publication.references.begin(), publication.references.end(), id) != publication.references.end()) {
            return pub_pair.first;
        }
    }

    return NO_PUBLICATION;
}

std::vector<std::pair<Year, PublicationID>> Datastructures::get_publications_after(AffiliationID affiliationid, Year year)
{
    std::vector<std::pair<Year, PublicationID>> result;

    for (const auto& pub_pair : publications) {
        const Publication& publication = pub_pair.second;

        if (std::find(publication.affiliations.begin(), publication.affiliations.end(), affiliationid) != publication.affiliations.end() && publication.year >= year) {
            result.push_back(std::make_pair(publication.year, pub_pair.first));
        }
    }

    std::sort(result.begin(), result.end(), [](const auto& a, const auto& b) {
        if (a.first == b.first) {
            return a.second < b.second;
        }
        return a.first < b.first;
    });

    return result;
}

std::vector<PublicationID> Datastructures::get_referenced_by_chain(PublicationID id)
{
    std::vector<PublicationID> chain;


    if (publications.find(id) == publications.end()) {
        chain.push_back(NO_PUBLICATION);
        return chain;
    }

    PublicationID parent = get_parent(id);

    if (parent != NO_PUBLICATION) {
        chain.push_back(parent);

        std::vector<PublicationID> parentChain = get_referenced_by_chain(parent);
        chain.insert(chain.end(), parentChain.begin(), parentChain.end());
    }

    return chain;
}

std::vector<PublicationID> Datastructures::get_all_references(PublicationID id)
{
    std::vector<PublicationID> allReferences;

    auto publication = publications.find(id);
    if (publication == publications.end()) {
        allReferences.push_back(NO_PUBLICATION);
        return allReferences;
    }

    std::function<void(PublicationID)> get_references_recursive = [&](PublicationID currentId) {
        const auto& publication = publications.find(currentId);
        if (publication != publications.end()) {
            for (const auto& reference : publication->second.references) {
                allReferences.push_back(reference);
                get_references_recursive(reference);
            }
        }
    };

    get_references_recursive(id);

    return allReferences;
}

std::vector<AffiliationID> Datastructures::get_affiliations_closest_to(Coord xy)
{
    std::vector<std::pair<AffiliationID, double>> distancePairs;
    distancePairs.reserve(affiliations.size());

    for (const auto& [id, affiliation] : affiliations) {
        double distance = std::hypot(xy.x - affiliation.getCoord().x, xy.y - affiliation.getCoord().y);
        distancePairs.emplace_back(id, distance);
    }

    std::partial_sort(distancePairs.begin(), distancePairs.begin() + std::min(3, static_cast<int>(distancePairs.size())),
                      distancePairs.end(),
                      [](const auto& a, const auto& b) {
                          return a.second < b.second;
                      });

    std::vector<AffiliationID> closestAffiliations;
    closestAffiliations.reserve(3);

    std::transform(distancePairs.begin(), distancePairs.begin() + std::min(3, static_cast<int>(distancePairs.size())),
                   std::back_inserter(closestAffiliations),
                   [](const auto& pair) {
                       return pair.first;
                   });

    return closestAffiliations;
}

bool Datastructures::remove_affiliation(AffiliationID id)
{
    auto it = affiliations.find(id);

    if (it != affiliations.end()) {
        affiliations.erase(it);
        return true;
    }

    return false;
}

PublicationID Datastructures::get_closest_common_parent(PublicationID id1, PublicationID id2)
{
    auto get_reference_chain = [this](PublicationID id) {
        std::vector<PublicationID> chain;
        std::unordered_set<PublicationID> visited;

        while (id != NO_PUBLICATION && visited.insert(id).second) {
            chain.push_back(id);
            id = get_parent(id);
        }

        return chain;
    };

    const auto chain1 = get_reference_chain(id1);
    const auto chain2 = get_reference_chain(id2);

    for (const auto& parent : chain1) {
        if (std::find(chain2.begin(), chain2.end(), parent) != chain2.end() && parent != id1 && parent != id2) {
            return parent;
        }
    }

    return NO_PUBLICATION;
}

bool Datastructures::remove_publication(PublicationID publicationid)
{
    auto publication_it = publications.find(publicationid);

    if (publication_it == publications.end()) {
        return false;
    }

    for (auto& [id, publication] : publications) {
        auto& references = publication.references;
        references.erase(std::remove(references.begin(), references.end(), publicationid), references.end());
    }



    publications.erase(publication_it);

    return true;
}


std::vector<Connection> Datastructures::get_connected_affiliations(AffiliationID id)
{
    std::vector<Connection> connectedAffiliations = {};

    std::vector<PublicationID> aff_publications = get_publications(id);

    for (const auto& publicationID : aff_publications) {
        std::vector<AffiliationID> publication_affiliations = get_affiliations(publicationID);

        for (const auto& affiliationID : publication_affiliations) {
            if (publication_affiliations.size() <= 1){
                return {};
            } else if (affiliationID != id) {
                bool connectionExists = false;
                for (auto& connection : connectedAffiliations) {
                    if ((connection.aff1 == id && connection.aff2 == affiliationID) ||
                        (connection.aff1 == affiliationID && connection.aff2 == id)) {
                        connection.weight += 1;
                        connectionExists = true;
                        break;
                    }
                }

                if (!connectionExists) {
                    Connection connection;
                    connection.aff1 = id;
                    connection.aff2 = affiliationID;
                    connection.weight = 1;
                    connectedAffiliations.push_back(connection);
                }
            }
        }
    }

    return connectedAffiliations;
}


std::vector<Connection> Datastructures::get_all_connections()
{
    std::vector<Connection> all_connections;

    for (const auto& [affiliationID, affiliation] : affiliations) {
        std::vector<Connection> current_connections = get_connected_affiliations(affiliationID);

        for (const auto& connection : current_connections) {
            Connection orderedConnection;
            orderedConnection.aff1 = std::min(connection.aff1, connection.aff2);
            orderedConnection.aff2 = std::max(connection.aff1, connection.aff2);
            orderedConnection.weight = connection.weight;

            bool connectionExists = false;
            for (const auto& existingConnection : all_connections) {
                if (existingConnection == orderedConnection) {
                    connectionExists = true;
                    break;
                }
            }

            if (!connectionExists) {
                all_connections.push_back(orderedConnection);
            }
        }
    }

    return all_connections;
}


Path Datastructures::get_any_path(AffiliationID source, AffiliationID target)
{
    std::queue<AffiliationID> queue;
    std::unordered_map<AffiliationID, AffiliationID> parent;
    std::unordered_map<AffiliationID, int> weights;

    queue.push(source);
    parent[source] = NO_AFFILIATION;
    weights[source] = 0;

    while (!queue.empty()) {
        AffiliationID current = queue.front();
        queue.pop();

        for (Connection neighbor : get_connected_affiliations(current)) {
            if (parent.find(neighbor.aff2) == parent.end()) {
                parent[neighbor.aff2] = current;
                weights[neighbor.aff2] = neighbor.weight;
                queue.push(neighbor.aff2);

                if (neighbor.aff2 == target) {
                    Path path;
                    AffiliationID temp = target;
                    while (temp != NO_AFFILIATION) {
                        AffiliationID parent_affiliation = parent[temp];
                        if (parent_affiliation != NO_AFFILIATION) {
                            Connection connection{parent_affiliation, temp, weights[temp]};
                            path.push_back(connection);
                        }
                        temp = parent_affiliation;
                    }
                    std::reverse(path.begin(), path.end());
                    return path;
                }
            }
        }
    }

    return {};
}

Path Datastructures::get_path_with_least_affiliations(AffiliationID /*source*/, AffiliationID /*target*/)
{
    // Replace the line below with your implementation
    throw NotImplemented("get_path_with_least_affiliations()");
}

Path Datastructures::get_path_of_least_friction(AffiliationID /*source*/, AffiliationID /*target*/)
{
    // Replace the line below with your implementation
    throw NotImplemented("get_path_of_least_friction()");
}

PathWithDist Datastructures::get_shortest_path(AffiliationID /*source*/, AffiliationID /*target*/)
{
    // Replace the line below with your implementation
    throw NotImplemented("get_shortest_path()");
}


